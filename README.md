# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 365
- HTTP: 130 alive / 77 gold
- HTTPS: 62 alive / 25 gold
- SOCKS4: 140 alive / 116 gold
- SOCKS5: 178 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47995
- Ever gold: 1508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
