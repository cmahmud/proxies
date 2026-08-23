# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 343
- HTTP: 117 alive / 41 gold
- HTTPS: 43 alive / 8 gold
- SOCKS4: 180 alive / 153 gold
- SOCKS5: 186 alive / 141 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32887
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
