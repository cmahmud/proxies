# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 390
- HTTP: 106 alive / 61 gold
- HTTPS: 44 alive / 9 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33321
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
