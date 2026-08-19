# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 530
- HTTP: 344 alive / 164 gold
- HTTPS: 232 alive / 87 gold
- SOCKS4: 194 alive / 137 gold
- SOCKS5: 224 alive / 142 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18650
- Ever gold: 725

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
