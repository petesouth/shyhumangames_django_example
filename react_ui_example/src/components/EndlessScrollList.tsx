import React, { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { Container, Row, Col } from 'react-bootstrap';
import { useSuppliers } from '../features/hooks';
import { RootState } from '../store';
import 'bootstrap/dist/css/bootstrap.min.css';

const EndlessScrollList: React.FC = () => {
    const { fetchSuppliers } = useSuppliers();
    const { suppliers, loading, error } = useSelector((state: RootState) => state.suppliers);

    useEffect(() => {
        fetchSuppliers('', '', null);
    }, [fetchSuppliers]);

    return (
        <Container fluid style={{ height: '100vh', overflow: 'auto' }}>
            {suppliers.map((supplier) => (
                <Row key={supplier.id} className="justify-content-md-center">
                    <Col xs={12} md={6} lg={4}>
                        <div className="panel" style={{ marginBottom: '20px', background: '#f8f9fa', padding: '20px' }}>
                            <h1>{supplier.name}</h1>
                        </div>
                    </Col>
                </Row>
            ))}
            {loading && <p>Loading more suppliers...</p>}
            {error && <p>Error: {error}</p>}
        </Container>
    );
};

export default EndlessScrollList;
