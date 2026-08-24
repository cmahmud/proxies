# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 386
- HTTP: 112 alive / 54 gold
- HTTPS: 70 alive / 14 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 195 alive / 163 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33380
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
