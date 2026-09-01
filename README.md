# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 459
- HTTP: 148 alive / 92 gold
- HTTPS: 123 alive / 34 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46866
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
