# SyndProxy private pool

## Current pool

- Alive now: 1453
- Gold now: 445
- HTTP: 551 alive / 104 gold
- HTTPS: 393 alive / 28 gold
- SOCKS4: 241 alive / 152 gold
- SOCKS5: 268 alive / 161 gold

## Historical pool

- Discovered: 159336
- Ever alive: 30482
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
