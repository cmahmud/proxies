# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 398
- HTTP: 190 alive / 72 gold
- HTTPS: 142 alive / 20 gold
- SOCKS4: 220 alive / 154 gold
- SOCKS5: 221 alive / 152 gold

## Historical pool

- Discovered: 149502
- Ever alive: 26737
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
