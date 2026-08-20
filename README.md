# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 386
- HTTP: 217 alive / 78 gold
- HTTPS: 171 alive / 22 gold
- SOCKS4: 214 alive / 146 gold
- SOCKS5: 193 alive / 140 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26929
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
