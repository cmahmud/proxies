# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 427
- HTTP: 304 alive / 85 gold
- HTTPS: 212 alive / 25 gold
- SOCKS4: 223 alive / 154 gold
- SOCKS5: 267 alive / 163 gold

## Historical pool

- Discovered: 163866
- Ever alive: 31990
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
