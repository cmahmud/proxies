# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 454
- HTTP: 112 alive / 87 gold
- HTTPS: 125 alive / 30 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46715
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
