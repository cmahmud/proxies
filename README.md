# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 258
- HTTP: 440 alive / 32 gold
- HTTPS: 172 alive / 5 gold
- SOCKS4: 228 alive / 116 gold
- SOCKS5: 234 alive / 105 gold

## Historical pool

- Discovered: 95405
- Ever alive: 10987
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
