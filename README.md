# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 429
- HTTP: 100 alive / 73 gold
- HTTPS: 72 alive / 24 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 181 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47680
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
