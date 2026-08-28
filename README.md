# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 367
- HTTP: 88 alive / 69 gold
- HTTPS: 82 alive / 11 gold
- SOCKS4: 164 alive / 144 gold
- SOCKS5: 173 alive / 143 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43180
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
