# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 380
- HTTP: 87 alive / 48 gold
- HTTPS: 47 alive / 13 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33556
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
