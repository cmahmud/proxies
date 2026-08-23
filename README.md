# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 386
- HTTP: 87 alive / 62 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 194 alive / 155 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33092
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
