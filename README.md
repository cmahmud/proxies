# SyndProxy private pool

## Current pool

- Alive now: 1289
- Gold now: 565
- HTTP: 474 alive / 193 gold
- HTTPS: 349 alive / 94 gold
- SOCKS4: 255 alive / 145 gold
- SOCKS5: 211 alive / 133 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22883
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
