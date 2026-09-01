# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 449
- HTTP: 111 alive / 78 gold
- HTTPS: 109 alive / 30 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 189 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47372
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
