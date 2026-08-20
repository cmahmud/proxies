# SyndProxy private pool

## Current pool

- Alive now: 792
- Gold now: 392
- HTTP: 197 alive / 76 gold
- HTTPS: 160 alive / 17 gold
- SOCKS4: 216 alive / 151 gold
- SOCKS5: 219 alive / 148 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26786
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
