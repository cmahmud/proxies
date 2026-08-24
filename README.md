# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 391
- HTTP: 127 alive / 57 gold
- HTTPS: 63 alive / 14 gold
- SOCKS4: 173 alive / 155 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33642
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
