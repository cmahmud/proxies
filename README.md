# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 443
- HTTP: 132 alive / 85 gold
- HTTPS: 147 alive / 23 gold
- SOCKS4: 186 alive / 164 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42237
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
