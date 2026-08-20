# SyndProxy private pool

## Current pool

- Alive now: 682
- Gold now: 384
- HTTP: 176 alive / 68 gold
- HTTPS: 105 alive / 18 gold
- SOCKS4: 196 alive / 143 gold
- SOCKS5: 205 alive / 155 gold

## Historical pool

- Discovered: 146601
- Ever alive: 25677
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
