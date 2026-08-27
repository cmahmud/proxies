# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 415
- HTTP: 110 alive / 77 gold
- HTTPS: 124 alive / 16 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42073
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
