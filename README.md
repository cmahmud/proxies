# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 535
- HTTP: 377 alive / 163 gold
- HTTPS: 254 alive / 88 gold
- SOCKS4: 199 alive / 140 gold
- SOCKS5: 229 alive / 144 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18649
- Ever gold: 725

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
