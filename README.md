# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 441
- HTTP: 127 alive / 84 gold
- HTTPS: 148 alive / 23 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42238
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
