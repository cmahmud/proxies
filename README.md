# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 440
- HTTP: 118 alive / 87 gold
- HTTPS: 144 alive / 22 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42248
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
