# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 422
- HTTP: 97 alive / 72 gold
- HTTPS: 37 alive / 16 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48942
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
