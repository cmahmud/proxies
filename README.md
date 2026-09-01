# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 459
- HTTP: 130 alive / 88 gold
- HTTPS: 129 alive / 32 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 189 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46700
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
