# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 450
- HTTP: 101 alive / 84 gold
- HTTPS: 56 alive / 30 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49198
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
