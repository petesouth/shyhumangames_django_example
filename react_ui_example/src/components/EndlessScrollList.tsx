import React, { useEffect, useRef, useCallback, useState } from 'react';
import { useSelector } from 'react-redux';
import { Container, Row, Col, Card, CardBody, CardHeader, CardText, Form, Button } from 'react-bootstrap';
import { useSuppliers } from '../features/hooks';
import { RootState } from '../store';
import 'bootstrap/dist/css/bootstrap.min.css';

interface SearchFormProps {
    nameSearch: string,
    cityNumber: string,
    onChangeName: (value: string)=> void,
    onChangeCityNumber: (value: string)=> void,
    onSubmit: ()=>void
}

const SearchForm = ({
    nameSearch,
    cityNumber,
    onChangeName,
    onChangeCityNumber,
    onSubmit
  }: SearchFormProps) => {


  return (
    <Card className="mb-4 shadow-sm"> {/* Add some shadow for depth */}
      <CardHeader>
        <h6 className="mb-0">ShyHumanGames: Endless Scroll Example</h6> {/* Ensure heading is centered if needed */}
      </CardHeader>
      <CardBody>
        <div>
          <Form.Group className="mb-3" controlId="nameSearch">
            <Form.Control type="text" value={nameSearch} onChange={(e)=>{
                onChangeName(e.target.value);
            }} placeholder="Name Search" />
          </Form.Group>
          <Form.Group className="mb-3" controlId="cityNumber">
            <Form.Control type="number" value={cityNumber} onChange={(e)=>{
                onChangeCityNumber(e.target.value);
            }} placeholder="City Number" />
          </Form.Group>
          <Form.Group className="mb-3 d-grid"> {/* Use Bootstrap's grid for button alignment */}
            <Button variant="primary" type="submit" onClick={()=>{
                onSubmit();
            }}> {/* Use a primary variant for better visibility */}
              Search
            </Button>
          </Form.Group>
        </div>
      </CardBody>
    </Card>
  );
};


const EndlessScrollList = () => {
    const { fetchSuppliers } = useSuppliers();
    const { suppliers, loading, error, hasMore, next } = useSelector((state: RootState) => {
        return state.suppliers;
    });

    const [nameSearch, setNameSearch] = useState<string>("");
    const [cityNumber, setCityNumber] = useState<string>("");

    const suppliersState = useSelector((state: RootState) => state.suppliers)
    const suppliersStateRef = useRef(suppliersState);

    console.log(suppliersState);

    const containerRef = useRef<HTMLDivElement | null>(null);

    const handleScroll = () => {
        const container = containerRef.current;
        if (container) {

            const isNearBottom = container.scrollTop + container.clientHeight >= container.scrollHeight - 20;
            if (isNearBottom && suppliersStateRef.current.hasMore && !suppliersStateRef.current.loading && suppliersStateRef.current.next !== null) {
                // Note: Ensure `next` is obtained correctly here, as it should come from suppliersStateRef.current.next
                fetchSuppliers('', '', suppliersStateRef.current.next);
            }
        }
    };

    useEffect(() => {
        suppliersStateRef.current = suppliersState;
    }, [suppliersState]);


    useEffect(() => {
        // Initial load
        if (suppliers.length < 1) {
            fetchSuppliers('', '', null);
        }

        const container = containerRef.current;
        if (container) {
            container.addEventListener('scroll', () => {
                handleScroll();
            });
        }

    }, []);

    return (
        <Container fluid style={{ height: '100vh', overflow: 'auto', paddingTop: 20 }} ref={containerRef}>
            <Row key={"searchRow"} className="justify-content-center" style={{paddingTop: 20, paddingBottom: 20}}> {/* Keeps horizontal centering */}
                <Col xs={12} md={6} lg={4}> {/* Removes vertical centering */}
                    <SearchForm nameSearch={nameSearch} cityNumber={cityNumber} onChangeName={(value: string): void => {
                        setNameSearch(value);
                    } } onChangeCityNumber={(value: string): void=> {
                        setCityNumber(value);
                    } } onSubmit={(): void => {
                        alert("Howdy: " + nameSearch + " " + cityNumber);
                    } } />
                </Col>
            </Row>
            {suppliers.map((supplier, index) => (
                <Row key={supplier.id} className="justify-content-center"> {/* Keeps horizontal centering */}
                    <Col xs={12} md={6} lg={4}> {/* Removes vertical centering */}
                        <Card className="panel" style={{ textAlign: "left", marginBottom: '20px', background: '#f8f9fa', padding: '20px' }}>
                            <CardHeader>
                                <h6>ID: {supplier.id}</h6>
                            </CardHeader>
                            <CardBody>
                                <CardText>Name: {supplier.name}</CardText>
                                <CardText>City: {supplier.city}</CardText>
                                <CardText>Popularity: {supplier.popularity}</CardText>
                                <CardText>Comments Count: {supplier.comments_count}</CardText>
                                <CardText>License Number: {supplier.license_number}</CardText>
                                <CardText>Rating Count: {supplier.rating_count}</CardText>
                                <CardText>Rating Score: {supplier.rating_score}</CardText>
                                <CardText>Status: {supplier.status}</CardText>
                            </CardBody>


                        </Card>
                    </Col>
                </Row>
            ))}
            {loading && <p>Loading more suppliers...</p>}
            {error && <p>Error: {error}</p>}
        </Container>


    );
};

export default EndlessScrollList;
