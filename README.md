# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 446
- HTTP: 112 alive / 85 gold
- HTTPS: 47 alive / 27 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 186 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49239
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
