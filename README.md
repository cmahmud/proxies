# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 398
- HTTP: 140 alive / 78 gold
- HTTPS: 184 alive / 22 gold
- SOCKS4: 165 alive / 146 gold
- SOCKS5: 172 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39947
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
