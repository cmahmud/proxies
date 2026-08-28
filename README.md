# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 391
- HTTP: 77 alive / 52 gold
- HTTPS: 75 alive / 16 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42871
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
