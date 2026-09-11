# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 444
- HTTP: 109 alive / 82 gold
- HTTPS: 45 alive / 28 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 180 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49211
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
