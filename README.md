# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 455
- HTTP: 121 alive / 83 gold
- HTTPS: 55 alive / 33 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 194 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49228
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
