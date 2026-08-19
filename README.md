# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 372
- HTTP: 280 alive / 90 gold
- HTTPS: 194 alive / 15 gold
- SOCKS4: 221 alive / 143 gold
- SOCKS5: 187 alive / 124 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18270
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
