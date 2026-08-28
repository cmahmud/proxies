# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 440
- HTTP: 117 alive / 87 gold
- HTTPS: 146 alive / 22 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 197 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42247
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
