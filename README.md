# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 530
- HTTP: 371 alive / 164 gold
- HTTPS: 247 alive / 93 gold
- SOCKS4: 230 alive / 148 gold
- SOCKS5: 201 alive / 125 gold

## Historical pool

- Discovered: 123228
- Ever alive: 18974
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
