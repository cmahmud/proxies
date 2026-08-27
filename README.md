# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 413
- HTTP: 116 alive / 68 gold
- HTTPS: 125 alive / 16 gold
- SOCKS4: 171 alive / 164 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41383
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
