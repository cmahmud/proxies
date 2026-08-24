# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 392
- HTTP: 114 alive / 57 gold
- HTTPS: 64 alive / 14 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33644
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
