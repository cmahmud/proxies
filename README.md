# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 422
- HTTP: 97 alive / 68 gold
- HTTPS: 39 alive / 19 gold
- SOCKS4: 187 alive / 164 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48958
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
