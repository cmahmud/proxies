# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 440
- HTTP: 125 alive / 84 gold
- HTTPS: 101 alive / 23 gold
- SOCKS4: 165 alive / 162 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34317
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
