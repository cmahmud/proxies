# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 420
- HTTP: 98 alive / 73 gold
- HTTPS: 46 alive / 23 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49480
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
