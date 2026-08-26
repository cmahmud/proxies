# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 419
- HTTP: 144 alive / 81 gold
- HTTPS: 164 alive / 24 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 185 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40300
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
