# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 450
- HTTP: 125 alive / 87 gold
- HTTPS: 52 alive / 31 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 180 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49281
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
