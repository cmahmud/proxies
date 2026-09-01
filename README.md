# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 473
- HTTP: 144 alive / 95 gold
- HTTPS: 123 alive / 41 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46934
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
