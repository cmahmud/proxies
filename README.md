# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 423
- HTTP: 116 alive / 75 gold
- HTTPS: 181 alive / 23 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40548
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
