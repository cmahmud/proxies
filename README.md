# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 442
- HTTP: 96 alive / 72 gold
- HTTPS: 111 alive / 31 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 187 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47450
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
