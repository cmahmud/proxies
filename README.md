# SyndProxy private pool

## Current pool

- Alive now: 819
- Gold now: 402
- HTTP: 245 alive / 91 gold
- HTTPS: 160 alive / 21 gold
- SOCKS4: 202 alive / 135 gold
- SOCKS5: 212 alive / 155 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27615
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
