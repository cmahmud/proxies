# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 386
- HTTP: 140 alive / 56 gold
- HTTPS: 45 alive / 13 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 197 alive / 161 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33654
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
