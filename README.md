# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 411
- HTTP: 101 alive / 66 gold
- HTTPS: 77 alive / 19 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35356
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
