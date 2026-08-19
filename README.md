# SyndProxy private pool

## Current pool

- Alive now: 1163
- Gold now: 392
- HTTP: 386 alive / 86 gold
- HTTPS: 264 alive / 22 gold
- SOCKS4: 225 alive / 137 gold
- SOCKS5: 288 alive / 147 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22160
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
