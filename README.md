# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 411
- HTTP: 109 alive / 68 gold
- HTTPS: 109 alive / 16 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42545
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
